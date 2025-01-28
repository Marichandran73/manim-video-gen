# AI Manim Video Generator

An AI tutor that generates [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) style videos for teaching and visualizing any concept. **This is a bare-bones version of the original [3Brown1Blue](https://github.com/christopherabey/3brown1blue) project**, without the additional unnecessary dependencies. Here's a demo:

https://github.com/christopherabey/3brown1blue/assets/50386081/87427cef-c2a4-4848-911d-749cd125e6fc


## How It Works

The system uses a multi-stage AI pipeline to generate educational videos:

1. **Transcript Generation**: An LLM generates a detailed script breaking down the concept into teachable segments
2. **Scene Generation**: Each segment is converted into scene descriptions with mathematical animations
3. **Parallel Rendering**: Multiple scenes are rendered simultaneously using subprocessing
4. **Error Handling**: Failed renders are fed back to the LLM for refinement until successful
5. **Video Compilation**: Successfully rendered scenes are combined into the final video


## Setup

### Backend Setup
1. Clone the repository
2. Navigate to the backend directory: `cd backend`
3. Run the setup script to install dependencies and create the virtual environment: `./setup.sh`

### Environment Variables
Create a `.env` file and follow the `.env.example` file to fill it out. At a minimum you need:
- `LLM_CLIENT`
- `LLM_MODEL`
- 1 LLM API Key
- LMNT API Key


## Usage

### Web Interface
1. Start the backend server: `cd backend && ./run.sh`
2. Start the frontend server in a separate terminal: `cd frontend/next && npm i && npm run dev`
3. Enter your topic and generate a video

### CLI Tool
Generate videos directly from the command line: `python cli.py "Your topic here" --output path/to/output.mp4`


## Citation
If you use this project in your work, please cite:

```
@misc{3brown1blue,
author = {Shah, Krish and Abey, Chris and Mujral, Hargun},
title = {3Brown1Blue: AI-Generated Educational Videos},
year = {2024},
publisher = {GitHub},
url = {https://github.com/christopherabey/3brown1blue}
}
```


## Credits
- Original creators: Krish Shah, Chris Abey, Hargun Mujral
- Thank you to [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) for inspiration