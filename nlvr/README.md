# The Cornell Natural Language Visual Reasoning (NLVR) Corpus v1.0
Website: http://lic.nlp.cornell.edu/nlvr/

The corpus and task are described in:
A Corpus of Natural Language for Visual Reasoning.
Alane Suhr, Mike Lewis, James Yeh, and Yoav Artzi.
In *Proceedings of the Conference of the Association for Computational Linguistics (ACL)*, 2017.
Paper: http://yoavartzi.com/pub/slya-acl.2017.pdf  
Supplementary material: http://yoavartzi.com/pub/slya-acl.2017.sup.pdf  

*Update*: As of July 29, 2022, the hidden test set is being released to the public and we will not be updating the leaderboard.

## Structure of repository

There are three subdirectories, one for each split of the data (train,
development, and public test).

In each of the split directories, there are two items:
* **.json** file, containing the labeled sentences, structured representations, and identifiers which can be used to match the example with its six PNG permutations.
* **images** subdirectory, containing the PNG images.

### JSON files
Each line includes one example, represented as a JSON object. The fields are:
* **sentence**: the sentence from the first stage of data collection.
* **identifier**: a two-part identifier, in the form n-m, where n is the identifier for the original presentation in the first stage of data collection (there are at most four examples in the set which has this number), and m is the position in the original presentation (0 = A, 1 = B, 2 = C, 3 = D). 
                   
  This identifier is used to match examples in this file with images in the images subdirectory. The image names are in the format split-n-m-k.png, where 0 <= k <= 5 (representing the six permutations of the boxes), and *split* is the split name (train, dev, test).
* **directory**: the directory that the images associated with this example are in. E.g., if directory = n and the file is dev.json, the images for the example will be located in directory dev/images/n.
* **label**: the final label for the example, true or false.
* **structured_rep**: the structured representation of the image, which is a list of length three. For each item in this list, which represents a box, there is another list of items (up to length eight). For each item, there is an x and y position (x_loc and y_loc), a type (the name of the shape), a color, and a size.
* **evals**: the set of validations done in the second stage of data collection. This is a dictionary mapping a rater identifier to their validation. The rater identifiers persist across all splits; i.e., rater r0 in train is the same rater as rater r0 in dev. 
             
  This is NOT the final label for the example. The final label is in the field **label**.

### Image subdirectories
These contain numbered subdirectories, each containing up to 1000 PNGs each. For the training and development splits, these subdirectories can be used as cross-validation splits -- all examples originally presented together are in the same numbered subdirectory, and all six images for an example are in the same numbered subdirectory.
  
For example, an example whose identifier is 72-0 has the PNGs 72-0-0 through 72-0-5. If all six of these PNGs are the numbered subdirectory 5, then the PNGs for examples 72-1, 72-2, and 72-3 are also in subdirectory 5. This is done to prevent information (either about the original presentation of the four examples or about the permutations of a specific example) from leaking between cross-validation splits.

### Evaluation scripts
We provide evaluation scripts for predictions. These scripts are metrics_images.py and metrics_structured_rep.py. We assume that you have a CSV that has one line per prediction. In the case of images, we assume one prediction per PNG file. Each line contains two values: the identifier (in the case of images, we assume this is the filename; in the case of structured representations, we assume this is simply the identifier) and the predicted value ("true" or "false", case insensitive). 

Each script takes two arguments. The first argument is your predictions file. The second argument is the JSON file for the subset of the data you are comparing against.

## Note about sampling a validation set:
The training set contains many examples which differ only in the order of the boxes. When selecting a validation set to use, we suggest choosing a set of subdirectories in train/images/ rather than sampling. We observed that certain models are able to perform well on randomly-sampled validation images, due to permutations of these images occurring in the training set, but generalize poorly to the development data.
