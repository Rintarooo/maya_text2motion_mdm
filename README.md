# Python script for text-to-motion in Maya

## Overview
This repo works on generating skelton with 3d motion from text prompt and retarget from skelton to human 3D model using HumanIK in Maya. 

I used MDM: Human Motion Diffusion Model[ICLR2023] for generating a json file.
This json file includes the following motion info(root translation, each joint's rotation from parent joint)

## Usage
Clone my MDM repo
```bash
git clone https://github.com/Rintarooo/motion-diffusion-model.git
cd motion-diffusion-model
git checkout vm
```

Now, you should follow Usage in README.md and generate json file in Docker container.

you can copy the script `create_skelton_hik_motion.py`.

And then, modify json path where your json path exists.

Then, launch Maya2024.

In main menu bar: Windows > General Editors > Script Editor. Now you paste copied scripts

Now you can see skleton with motion.


Firstly, create human 3d model(in this case, MonsterWolfman).

Go to window>content browser>MonsterWolfman.ma, double click.

Then, change MonsterWolfman from A pose to T pose for retargeting

