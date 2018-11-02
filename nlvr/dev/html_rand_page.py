import json
import os
import random

images_dir = "images"
prefix = "https://raw.githubusercontent.com/cornell-lic/nlvr/master/dev/"

objs = [json.loads(line) for line in open("dev.json").readlines()]

random.shuffle(objs)

page = open("examples.html", "w")
page.write("<html>")
page.write("<head><link href=\"css/bootstrap.min.css\" rel=\"stylesheet\"></head>")
page.write("<body><center>")
page.write("<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js\"></script>")
page.write("<script src=\"js/bootstrap.min.js\"></script>")

for obj in objs:
  sentence = obj["sentence"]
  label = obj["label"]
  identifier = obj["identifier"]

  permutation = random.randint(0,5)

  filename = "dev-" + identifier + "-" + str(permutation) + ".png"

  path = ""
  for subdir in os.listdir(images_dir):
    full_subdir = os.path.join(images_dir, subdir)
    if os.path.isdir(full_subdir):
      for prop_file in os.listdir(full_subdir):
        if prop_file == filename:
          path = prefix + full_subdir + "/" + filename
          break
  
  labelstr = ""
  if label == "true":
    labelstr = "<span class = \"label label-success\">true</span>"
  else:
    labelstr = "<span class = \"label label-danger\">false</span>"
  page.write("<img src=\""+ path + "\"  style=\"border: #000000 1px outset; width: 450px;\"/><br /><table width = \"450px\"><tr><td>" + sentence + "</td><td>" + labelstr + "</td></tr></table><br /><br />\n")

page.write("</center>\n</body>\n</html>")

