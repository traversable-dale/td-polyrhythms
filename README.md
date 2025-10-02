Polyrhythm Visualizer – README

This project is a TouchDesigner-based audiovisual system that combines polyrhythmic beats, generative visuals, and audio playback into a cohesive interactive experience. It includes several core components, custom extensions, and DAT scripts to handle startup, UI, timing, and audio logic.

📂 Project Components
op.config

Handles startup logic and initialization.

Hosts timers used for splash sequences and GUI transitions:

timer_splash_startup

timer_splash_exit

timer_GUI_open

Controls project resolution and global settings.

op.ctrl

Holds all UI elements for user control.

Currently includes slider_speed for adjusting the system tempo.

op.vis

The main visual output of the project.

Contains polyrhythmic base visualizers (4 layers) and compositing for the final image.

op.colors (within op.vis)

Defines 4 beat-linked colors, one for each rhythmic base.

A 5th color defines the background.

op.beat

Generates polyrhythms using LFOs and counters.

Provides rhythm data that drives both visuals and audio.

op.shapes

Produces circle-based shapes orbiting a center point.

Includes feedback trails for layered motion effects.

op.background

TOP network that renders the project’s dynamic background visuals.

op.audio

Contains audio file playback.

Extension (module_audio.py) provides Python functions for starting and stopping all audio.

op.splash

Displays the splash screen graphic at startup.

Includes a button to start the application.

🐍 Python Extensions
module_GUI.py

module_GUI

Manages GUI and splash screen behavior.

Functions:

Test() – debug function.

Startup() – launches the splash screen and initializes timers.

ExitSplash() – triggers the exit splash timer.

OpenProgram() – reveals main GUI, visuals, and begins audio playback.

module_audio.py

module_audio

Controls playback of all audio operators listed in select_audio_files.

Functions:

StopAudio() – stops all audio operators by setting play = 0.

PlayAudio() – starts all audio operators by setting play = 1.

📑 DAT Scripts

chopexec_slider_speed.py – CHOP Execute script tied to slider_speed. Handles updates to tempo when the slider changes.

execute_config.py – DAT Execute script for startup/shutdown logic in op.config.

timer_GUI_open_callbacks.py – Callbacks for opening the GUI after splash.

timer_splash_wait_callbacks.py – Callbacks for timing delays during splash.

timer_splash_exit_callbacks.py – Handles logic when the splash screen closes.

timer_splash_startup_callbacks.py – Handles startup timing and transitions into main program.

🚀 Startup Sequence

On launch, op.config runs Startup() (via module_GUI).

The splash screen (op.splash) is displayed.

Timers (timer_splash_startup, timer_splash_exit, etc.) handle delays and transitions.

Once the splash is done, OpenProgram() is called:

GUI (op.GUI) is revealed.

Visuals (op.vis) fade in.

Audio playback starts (PlayAudio()).

🎛 Controls

Slider Speed (op.ctrl/slider_speed) – adjusts rhythm speed/tempo.

Splash Screen Button (op.splash/start) – begins the program.