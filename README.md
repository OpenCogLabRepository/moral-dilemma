# Moral Dilemma Task

This is a [PsychoPy](http://www.psychopy.org/) implementation of the Moral Dilemma task described in [Harrison et al. 2008](http://www.pnas.org/content/105/28/9781.long#sec-13) and in particular in the [Supporting Information Materials and Methods](http://www.pnas.org/content/suppl/2008/07/18/0711791105.DCSupplemental/0711791105SI.pdf#nameddest=STXT) and [Supporting Information Appendix](http://www.pnas.org/content/suppl/2008/07/18/0711791105.DCSupplemental/Appendix_PDF.pdf).

Harrison, B.J., Pujol, J., Lopez-Sola, M., Hernandez-Ribas, R., Deus, J., Ortiz, H., Soriano-Mas, C., Yucel, M., Pantelis, C., Cardoner, N., 2008. *Consistency and Functional Specialization in the Default Mode Brain Network.* Proceedings of the National Academy of Sciences 105, 9781--9786. doi:10.1073/pnas.0711791105

Prior to the experiment, participants are familiarized with the vignettes by listening to a recording of the vignette while viewing a corresponding image (see Fig 1a and 1b for examples) and thinking about how they would react in the scenario (```moral_dilemma_training.py```). If the training occurs several hours or days prior to the experiment, they should be questioned to verify that they remember the details of the vignettes.

![Fig. 1 Example of control vignette.](images/c1.JPG?raw=true "Fig. 1 Example of control vignette.")
Fig. 1 Example of a control vignette. *Does he make the basket?*

![Fig. 2 Example of a dilemma vignette.](images/d1.JPG?raw=true "Fig 2. Example of dilemma vignette.")
Fig. 2 Example of a dilemma vignette. *Would you push the chair?* To hang your son and save the lives of five other prisoners.

The experiment (```moral_dilemma.py```) consists of 24 moral dilemma questions and 24 control questions presented in eight 30-second blocks, each consisting of six questions, that alternated between control (C) and moral dilemma (D) conditions (CDCDCDCD). During each stimuli, participants view an image and hear a question corresponding to each vignette. Each image is displayed for 5 seconds and the audio begins one second after image onset. Participants respond to the proposed question by pressing one of two buttons on a response box (index finger button for “yes”, middle finger button for “no”). The task begins and ends with 20 second fixation blocks during which participants passively view a plus (+) sign centered on a grey background.
