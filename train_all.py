
import os

if __name__ == "__main__":
    
    # $$$$ EDIT THESE PARAMETERS $$$$

    # Choose the Models you want to use:
    # Create a list of strings from 1 -> 6 for all, the key below is for which model(s) you want to use
    # Models
    # 1 = GATraj
    # 2 = SocialGAN2
    # 3 = Social-STGCNN
    # 4 = SocialLSTM
    # 5 = STAR
    # 6 = STGAT
    models = ['1', '2', '3', '4', '5', '6']
    #models = ['6']

    # Enter your username here for your machine. i.e. /home/morgan/Desktop
    # Input what your machine says instead of morgan
    user = 'morgan'
    # Choose epochs and batch size
    epochs = '250'
    batch_size = '64'
    # Choose the dataset you want to train on
    # data_set_char = eth, hotel, zara1, zara2, univ
    data_set_char = 'eth'



    # $$$$ LEAVE EVERYTHING AFTER THIS ALONE $$$$
    # data_set_num = 0, 1, 2, 3, 4
    if data_set_char == 'eth':
        data_set_num = '0'
    elif data_set_char == 'hotel':
        data_set_num = '1'
    elif data_set_char == 'zara1':
        data_set_num = '2'
    elif data_set_char == 'zara2':
        data_set_num = '3'
    elif data_set_char == 'univ':
        data_set_num = '4'
    

    script_content = '#!/bin/bash\n\n'

    # Replace 'your_venv_path' with the actual path to your virtual environment
    #venv_path = '/home/' + user + '/Desktop/Trajectory_GANS/venv'

    activate_venv_command = 'source /home/' + user + '/Desktop/Trajectory_GANS/venv/bin/activate\n'
    
    script_content += activate_venv_command
    
    root_command = 'cd \n'
    for i in range(0, len(models)):
        if models[i] == '1':
    
            # GATraj

            script_content += root_command

            GATraj_command = 'cd /home/' + user + '/Desktop/Trajectory_GANS/GATraj\n'

            script_content += GATraj_command

            GATraj_train = "python train.py --test_set " + data_set_num + " --num_epochs " + epochs + " --x_encoder_layers 3 --eta_min 1e-5  --batch_size " + batch_size + "\
            --learning_rate 5e-4  --randomRotate True --final_mode 20 --neighbor_thred 10\
            --using_cuda True --clip 1 --pass_time 2 --ifGaussian False --SR True --input_offset True\n"
            
            script_content += GATraj_train

        elif models[i] == '2':
    
            # SocialGAN2
            script_content += root_command

            SocialGAN2_command = 'cd /home/' + user + '/Desktop/Trajectory_GANS/SocialGAN2\n'

            script_content += SocialGAN2_command

            SocialGAN2_train = "python train.py --dataset_name " + data_set_char + " --num_epochs " + epochs + " --batch_size " + batch_size + "\n"

            script_content += SocialGAN2_train

        elif models[i] == '3':

            # Social-STGCNN
            script_content += root_command

            SocialSTGCNN_command = 'cd /home/' + user + '/Desktop/Trajectory_GANS/Social-STGCNN\n'

            script_content += SocialSTGCNN_command

            SocialSTGCNN_train = "CUDA_VISIBLE_DEVICES=0 python3 train.py --lr 0.01 --n_stgcnn 1 --n_txpcnn 5 --batch_size " + batch_size + " --dataset " + data_set_char + " --tag social-stgcnn-" + data_set_char + " --use_lrschd --num_epochs " + epochs + " && echo '" + data_set_char + " Launched.' & P0=$!\n"

            script_content += SocialSTGCNN_train

            finish = "wait $P0\n"

            script_content += finish

        elif models[i] == '4':

            # SocialLSTM
            # Can't control batch_size for this one
            script_content += root_command

            SocialLSTM_command = 'cd /home/' + user + '/Desktop/Trajectory_GANS/SocialLSTM\n'

            script_content += SocialLSTM_command

            SocialLSTM_train = "python3 main.py 's' --dataset " + data_set_char + " --epoch " + epochs + "\n"

            script_content += SocialLSTM_train

        elif models[i] == '5':

            # STAR
            script_content += root_command

            STAR_command = 'cd /home/' + user + '/Desktop/Trajectory_GANS/STAR\n'

            script_content += STAR_command

            STAR_train = "python trainval.py --test_set " + data_set_char + " --num_epochs " + epochs + " --batch_size " + batch_size + "\n"

            script_content += STAR_train

        elif models[i] == '6':

            # STGAT
            script_content += root_command

            STGAT_command = 'cd /home/' + user + '/Desktop/Trajectory_GANS/STGAT\n'

            script_content += STGAT_command

            STGAT_train = "python train.py --dataset_name " + data_set_char + " --num_epochs " + epochs + " --batch_size " + batch_size + "\n"

            script_content += STGAT_train
    

    # Write all of these commands to a bash file to run every model

    script_file_path = '/home/' + user + '/Desktop/Trajectory_GANS/train_all.sh'

    with open(script_file_path, "w") as script_file:
        script_file.write(script_content)

    os.system(f"chmod +x {script_file_path}")

    os.system(f"{script_file_path}")


