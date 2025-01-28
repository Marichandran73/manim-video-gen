import argparse
import asyncio
from transcript_generator import TranscriptGenerator
from scene_generator import SceneGenerator
from logger import logger
import os
from dotenv import load_dotenv

load_dotenv()

async def generate_video(topic: str) -> str:
    """
    Generates a video from the given topic
    :param topic: Topic to generate video about
    :return: Path to the generated video file
    """
    # Generate transcript
    transcript_generator = TranscriptGenerator()
    transcriptions = await transcript_generator.generate_transcript(topic)
    
    # Generate scenes and video
    scene_generator = SceneGenerator(transcriptions)
    video_id = await scene_generator.generate_all_scenes()
    
    # Get the path to the final video
    video_path = f"generated/{video_id}/final_video.mp4"
    
    if not os.path.exists(video_path):
        raise Exception(f"Video generation failed - file not found at {video_path}")
    
    return video_path

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate an educational video from a topic')
    parser.add_argument('topic', type=str, help='The topic to generate a video about')
    parser.add_argument('--output', '-o', type=str, help='Output path for the video (optional)')
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Generate the video
        video_path = asyncio.run(generate_video(args.topic))
        
        # If output path is specified, copy the video there
        if args.output:
            import shutil
            output_path = args.output
            # Ensure the output directory exists
            os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
            shutil.copy2(video_path, output_path)
            print(f"Video successfully generated and saved to: {output_path}")
        else:
            print(f"Video successfully generated at: {video_path}")
            
    except Exception as e:
        logger.error(f"Error generating video: {str(e)}")
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main() 