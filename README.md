# Python script for text-to-motion in Maya

https://github.com/Rintarooo/maya_text2motion_mdm/assets/51239551/15a428dd-3b46-4971-a64b-393aa3c325cc



https://github.com/Rintarooo/maya_text2motion_mdm/assets/51239551/ba86a1e7-dbcb-426a-b98e-c39407b10fae



## Overview
This repo works on generating skelton with 3d motion from text prompt and retarget motion from skelton to human 3D model using HumanIK in Maya. 

I used MDM: Human Motion Diffusion Model[ICLR2023] for generating a json file.
This json file includes the following motion info(root translation, each joint's rotation from parent joint)

## Usage

### generate json file
Clone my MDM repo
```bash
git clone https://github.com/Rintarooo/motion-diffusion-model.git
cd motion-diffusion-model
git checkout vm
```

Now, you should follow Usage in README.md and generate json file in Docker container.

### generate skelton with motion in Maya using python script
you can copy the script `create_skelton_hik_motion.py`.

And then, modify json path where your json path exists.

Then, launch Maya2024.

In main menu bar: Windows > General Editors > Script Editor. Now you paste copied scripts

Now you can see skleton with motion.


### retargeting motion using HumanIK
Firstly, create human 3d model(in this case, MonsterWolfman).

Go to window>content browser>MonsterWolfman.ma, double click.

Then, change MonsterWolfman from A pose to T pose for retargeting.

And now you can use QucikRig for MonsterWolfman.




