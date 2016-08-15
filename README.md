[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.60144.svg)](http://dx.doi.org/10.5281/zenodo.60144)

# Moral Dilemma Task

Clemens C. C. Bauer<sup>1,2</sup> and R. Cameron Craddock<sup>3,4,†</sup>

<sup>1</sup>Department of Brain and Cognitive Sciences, Massachusetts Institute of Technology, Boston, MA,
<sup>2</sup>Center for Mindfulness, University of Massachusetts Medical School, Boston, MA,
<sup>3</sup>Nathan S. Kline Institute for Psychiatric Research, Orangeburg, NY, <sup>4</sup>Child Mind Institute, New York, NY

<sup>†</sup>Contact [cameron.craddock@childmind.org](mailto:cameron.craddock@childmind.org) with any comments or questions.

## Task Description

This is a [PsychoPy](http://www.psychopy.org/) implementation of the Moral Dilemma task described in [Harrison et al. 2008](http://www.pnas.org/content/105/28/9781.long#sec-13) and in particular in the [Supporting Information Materials and Methods](http://www.pnas.org/content/suppl/2008/07/18/0711791105.DCSupplemental/0711791105SI.pdf#nameddest=STXT) and [Supporting Information Appendix](http://www.pnas.org/content/suppl/2008/07/18/0711791105.DCSupplemental/Appendix_PDF.pdf).

Harrison, B.J., Pujol, J., Lopez-Sola, M., Hernandez-Ribas, R., Deus, J., Ortiz, H., Soriano-Mas, C., Yucel, M., Pantelis, C., Cardoner, N., 2008. *Consistency and Functional Specialization in the Default Mode Brain Network.* Proceedings of the National Academy of Sciences 105, 9781--9786. doi:10.1073/pnas.0711791105

Prior to the experiment, participants are familiarized with the vignettes by listening to a recording of the vignette while viewing a corresponding image (see Fig 1a and 1b for examples) and thinking about how they would react in the scenario (```moral_dilemma_training.py```). If the training occurs several hours or days prior to the experiment, the participant should be questioned just before performing the experiment to verify that they remember the details of the vignettes.

![Fig. 1 Example of vignettes.](examples.png?raw=true "Fig. 1 Example of vignettes.")

*Figure 1. Examples of task vignettes. A) A control vignette: "Mr. Jones is practicing his three-point
throw on the basketball court behind his
house. He hasn’t managed to score a
basket during the whole morning, despite
all the practice. He concentrates hard and
throws the ball one more time. This time
his aim is more accurate, the ball curves
through the air and falls cleanly into the
basket. Mr. Jones has managed to score a
basket for the first time."
Question during task:* ***Will he score?*** *B) A dilemma vignette. "Mr. Jones and his only son are held in a
concentration camp. His son tries to escape
but he is caught. The guard watching them
tells Mr. Jones that his son is going to be
hanged and that it will be him (Mr. Jones)
who has to push the chair. If he does not
do it, not only will his son die but also five
more people held in the concentration
camp." Question during task:* ***Would you push the
chair?***

The experiment (```moral_dilemma.py```) consists of 24 moral dilemma questions and 24 control questions presented in eight 30-second blocks, each consisting of six questions, that alternated between control (C) and moral dilemma (D) conditions (CDCDCDCD). During each stimuli, participants view an image and hear a question corresponding to each vignette. Each image is displayed for 5 seconds and the audio begins one second after image onset. Participants respond to the proposed question by pressing one of two buttons on a response box (index finger button for “yes”, middle finger button for “no”). The task begins and ends with 20 second fixation blocks during which participants passively view a plus (+) sign centered on a grey background.

## Example fMRI Activations

A group-level analysis of 124 participants from the openly shared [Enhanced Nathan Kline Institute - Rockland Sample Neurofeedback study](http://fcon_1000.projects.nitrc.org/indi/enhanced/) resulted in the Dilemma > Control activation pattern depicted in Figure 2a (p<0.001 TFCE FWE-corrected). Figure 2b illustrates the overlap of individual level results, each of which were corrected at p<0.05, uncorrected.

![Fig. 2 Areas activated in the Dilemma > Control contrast.](task_results.png?raw=true "Fig. 2 Areas activated in the Dilemma > Control contrast.")

*Figure 2. Areas activated in the Dilemma > Control contrast. A. Results of group-level analysis, thresholded at p<0.001 TFCE FWE-corrected. B. Overlap of individual level results, each thresholded at p<0.05 uncorrected.*

## Usage Notes

This task requires that the [PsychoPy](http://www.psychopy.org/) ecosystem be installed either as python libraries, or as a standalone application (available for Mac OSX and Microsoft Windows). For Debian systems (including Ubuntu), PsychoPy can be easily installed via [NeuroDebian](http://neuro.debian.net/pkgs/psychopy.html?highlight=psychopy).

The task can work with a keyboard (1 is yes, 2 is no) or a Lumina button box. Once started, the task will ask the user to input a participant ID, which will be used for naming the output files, and a volume level. Max volume is 1.0 and the minimum is 0.0. Once running, the task will pause on the instruction screen until any key is pressed on the keyboard, or a trigger is received through the Lumina system (e.g., for use during an fMRI).

The task will create a Data/ directory in the current directory to store participant responses. Responses will be stored in a file whose name includes the participant ID entered by the user and the data and time the task was started.

## Scoring Responses
Responses and response times can be extracted from logfiles using the ```morald_extract_timings_responses_csv.py``` Python script. This script requires the [Pandas](http://pandas.pydata.org/) library and that ```morald_qtimes.txt``` is installed in the same directory as the script. The values in the ```morald_qtimes.txt``` file are used to adjust the reaction times for the length of the audio question prompt and norm the responses based on the response rates reported in the [Supporting Information Appendix](http://www.pnas.org/content/suppl/2008/07/18/0711791105.DCSupplemental/Appendix_PDF.pdf) for [Harrison et al. 2008](http://www.pnas.org/content/105/28/9781.long#sec-13).

## Acknowledgements
Salary support was provided by NIMH BRAINS R01MH101555 to RCC.
