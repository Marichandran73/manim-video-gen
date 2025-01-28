from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
from pydantic import BaseModel
from transcript_generator import TranscriptGenerator
from scene_generator import SceneGenerator
from logger import logger

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Hello world"}

@app.post("/generate/")
async def generate(request: VideoRequest):
    """
    Takes in a topic and returns a video id for the generated video
    """
    text = request.text
    transcript_generator = TranscriptGenerator()
    transcriptions = await transcript_generator.generate_transcript(text)
    scene_generator = SceneGenerator(transcriptions)
    video_id = await scene_generator.generate_all_scenes()

    return {"video_id": video_id, "text": "\n".join(transcriptions)}

# For testing purposes
@app.post("/generate_stub")
async def generate_stub(request: VideoRequest):
    """
    Takes in a topic and returns a video id for the generated video
    """
    return {"video_id": "0dc1c87d-f027-43be-b443-2d573b03ab7a", "text": "This is a stub"}

@app.get("/videos/{video_id}")
async def get_video(video_id: str):
    """
    Returns the video with the given video_id
    """
    video_path = f"generated/{video_id}/final_video.mp4"
    def iterfile():
        with open(video_path, mode="rb") as file_like:
            yield from file_like

    return StreamingResponse(iterfile(), media_type="video/mp4")
