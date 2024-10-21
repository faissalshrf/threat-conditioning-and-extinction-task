# Threat Conditioning and Extinction Task (TCET) [English/Mandarin Chinese]

## Overview
The Threat Conditioning and Extinction Task (TCET) is a three-phase task designed to assess participants' emotional responses to faces during **Preconditioning**, **Conditioning**, and **Extinction** phases. Faces are displayed, and participants rate their emotional response to the faces on a scale from negative to positive. In the conditioning phase, a subset of faces are paired with an unconditioned stimulus (UCS), either a negative scream or a positive laugh, presented with an 80% likelihood.

</br>
<p align="center">
  <img src="https://github.com/user-attachments/assets/0c5b17d5-78f3-4c85-8a23-9f83e9219044" alt="figureTCET-1" height="300"/>
</p>
</br>



## Phases Breakdown
1. **Preconditioning Phase**:
    - Neutral faces are shown without any emotional expressions.
    - The goal is to familiarize participants with the stimuli.

2. **Conditioning Phase**:
    - Two of the faces transition into either a negative or positive expression (screaming/laughing), accompanied by the respective sound (UCS).
    - The UCS appears 80% of the time.
    - The faces shown remain the same as in the preconditioning phase but with emotional transformations.

3. **Extinction Phase**:
    - Faces from the conditioning phase are shown again but without the emotional transformation.
    - The UCS is no longer presented, allowing for extinction of the conditioned response.

4. **Trigger Faces**:
    - An additional face appears randomly during each phase, and participants must click on it as fast as possible. This serves as an attention check.

## Data Collection
- After each phase, participants are asked to rate the emotional valence of the faces from 0 (negative) to 10 (positive) using a slider scale.
- Data is saved in Excel files for each phase of the experiment. The files include information about the mouse clicks, ratings, and response times.

<p align="center">
  <img src="https://github.com/user-attachments/assets/df76a93d-ab5c-4d98-9ded-1c0592c21e54" alt="Screenshot 2023-06-28" height="300"/>
</p>

## File Structure
- **/data/**: Contains the participant data collected during the task.
- **/schedules/**: Contains the schedule files for the different phases of the task, in `.xlsx` format.
    - `0_Instructions.xlsx`: Instructions for the participants.
    - `1_PreCondition.xlsx`: Stimuli presentation order for the preconditioning phase.
    - `2_Condition.xlsx`: Stimuli presentation order for the conditioning phase.
    - `3_Extinction.xlsx`: Stimuli presentation order for the extinction phase.
    - `4_Rating.xlsx`: Rating instructions for the participants after each phase.
- **/sound/**: Contains the UCS sound files (e.g., screaming and laughing sounds).
- **/stimuli/**: Contains the images used for the faces in BMP format.
- **`TCET_Sharif.psyexp`**: PsychoPy experiment file.
- **`TCET_Sharif.py`**: Python script generated by PsychoPy for running the experiment.

## Instructions for Running the Experiment
1. Open the `TCET_Sharif.psyexp` file in PsychoPy.
2. Ensure that the correct version of PsychoPy (2023.1.1 or higher) is installed.
3. Ensure all required files (schedules, stimuli, and sounds) are in their respective folders.
4. Run the experiment by clicking the "Run" button in the PsychoPy interface.

## Additional Information
- The experiment includes mouse click events to monitor response times for trigger faces.
- Ensure sound is enabled for the UCS auditory stimuli during the conditioning phase.
- The experiment is designed to run in English and Chinese, with the instructions and rating tasks available in both languages.

## References
- This TCET is an adjusted version of the task used by [Abend et al. (2020)](https://pubmed.ncbi.nlm.nih.gov/31955915/), based on the original design by [Lau et al. (2008)](https://pubmed.ncbi.nlm.nih.gov/18174830/).

## Contact
For questions or issues regarding the experiment, please contact [**Faissal Sharif**](mailto:faissal.sharif@stx.ox.ac.uk).
