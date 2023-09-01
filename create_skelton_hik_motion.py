import maya.cmds as cmds
import maya.mel as mel
import json

# Mapping of SMPL joint index to HIK joint Name
JOINT_MAP = [
    'Hips',
    'LeftUpLeg',
    'RightUpLeg',
    'Spine',
    'LeftLeg',
    'RightLeg',
    'Spine1',
    'LeftFoot',
    'RightFoot',
    'Spine2',
    'LeftToeBase',
    'RightToeBase',
    'Neck',
    'LeftShoulder',
    'RightShoulder',
    'Head',
    'LeftArm',
    'RightArm',
    'LeftForeArm',
    'RightForeArm',
    'LeftHand',
    'RightHand'
    ]

def create_human_ik_skeleton(character_name):
    # HumanIKのウィンドウを開く
    mel.eval('HIKCharacterControlsTool')

    # キャラクターを作成
    character = cmds.character(name=character_name)

    # HIKキャラクターノードを取得
    hik_character_node = character

    # スケルトンの作成
    mel.eval('hikCreateSkeleton;')

    return hik_character_node

def delete_joint(joint_name):
    if cmds.objExists(joint_name):
        # cmds.delete(joint_name)
        cmds.removeJoint(joint_name)
        print("Deleted joint: " + joint_name)
    else:
        print("Joint not found: " + joint_name)

def delete_finger():
    # 削除するジョイント名を指定して関数を呼び出す
    joint_del_lis = ["Character1_LeftHandThumb1", "Character1_LeftHandIndex1", "Character1_LeftHandMiddle1",
                    "Character1_LeftHandRing1", "Character1_LeftHandPinky1", "Character1_RightHandThumb1",
                    "Character1_RightHandIndex1", "Character1_RightHandMiddle1", "Character1_RightHandRing1", "Character1_RightHandPinky1"]
    # delete_joint("Character1_Hips")
    finger_lis = ["Thumb", "Index", "Middle","Ring", "Pinky"]
    left_right_lis = ["Left", "Right"]
    joint_del = []
    for i in range(5):
        finger = finger_lis[i]
        for k in range(2):
            left = left_right_lis[k]
            tmp_lis = ["Character1_" + left + "Hand" + finger + str(i) for i in range(1, 5)]# Thumb1 ~ Thumb4
            joint_del_lis = joint_del_lis + tmp_lis

    for joint_del in joint_del_lis:
       delete_joint(joint_del)

def make_anima(data):
    nreps = len(data["thetas"])
    ani = data["thetas"][0]# 1st nreps
    nframes = len(ani)
    njoints = len(ani[0])
    ntheta = len(ani[0][0])

    # print("nframes: ", nframes)
    # print("njoints: ", njoints)
    # print("ntheta: ", ntheta)

    # フレーム1でのジョイントの回転角度と並進移動量を設定
    ani_theta = data["thetas"][0]# 1st nreps
    ani_trans = data["translation"][0]# 1st nreps
    for k in range(nframes):
    # for k in range(2):
        ani_theta_k = ani_theta[k]# k frame (24, 3) deg
        ani_trans_k = ani_trans[k]# k frame (22, 3) xyz move
        # https://chayarokurokuro.hatenablog.com/entry/2020/01/18/024726
        # ani_theta_k[[0,1,2,...,23],:]
        # ani_theta_k[[0,1,2,...,23],:]
        # for i, joint in enumerate(JOINT_MAP):
        for i in range(22):
            joint_name_ch = "Character1_" + JOINT_MAP[i]
            cmds.setKeyframe(joint_name_ch, time=k+1, attribute='rotateX', value=ani_theta_k[i][0])
            cmds.setKeyframe(joint_name_ch, time=k+1, attribute='rotateY', value=ani_theta_k[i][1])
            cmds.setKeyframe(joint_name_ch, time=k+1, attribute='rotateZ', value=ani_theta_k[i][2])
            if joint_name_ch == "Character1_Hips":
                cmds.setKeyframe(joint_name_ch, time=k+1, attribute='translateX', value=5*ani_trans_k[i][0])
                cmds.setKeyframe(joint_name_ch, time=k+1, attribute='translateY', value=5*ani_trans_k[i][1])
                cmds.setKeyframe(joint_name_ch, time=k+1, attribute='translateZ', value=5*ani_trans_k[i][2])



    # タイムスライダーの範囲を設定
    # cmds.playbackOptions(min=0, max=2)
    cmds.playbackOptions(min=1, max=nframes)

    # # タイムライン上でアニメーションを確認
    cmds.play(forward=True)


if __name__ == "__main__":
    character_name = "MyCharacter"
    hik_character_node = create_human_ik_skeleton(character_name)
    print("HumanIKキャラクターノード: ", hik_character_node)

    delete_finger()


    # modify as your json path exists
    file_path = '###/json/motion_humanik.json'

    with open(file_path, 'r') as f:
        data = json.load(f)

    make_anima(data)