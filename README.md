# D&D Dice Roller

This D&D Dice Roller is a simple Python script that allows you to simulate rolling dice based on Dungeons & Dragons (D&D) rules. It calculates the number of natural 1s, natural 20s, and the average score of rolls with advantage, disadvantage, and normal rolls.
The idea was inspired by an argument during a game, on whether rolling physical dice produces different results compared to using a computer-based random function. This script seeks to provide insights into this debate by conducting a comparative analysis.
Although nobody has the time to roll thousands of dices and compare results, you can verify that there is a significat difference when using a peudo random algoritm after rolling 50 dices or so, as the results from this script are more flattened out in comparrison to the physical dice rolls.

# Usage
1. Make sure you have Python installed on your system.
2. Clone the repository or download the dnd_dice_roller.py file.
3. Open a terminal or command prompt and navigate to the directory containing dnd_dice_roller.py.
4. Run the script by executing the following command:
```
python dnd_dice_roller.py
```
Follow the on-screen instructions to input the number of rolls.
The script will display the results, including the number of natural 1s, natural 20s, and the average score for advantage, disadvantage, and normal rolls.


# UPDATE

I've added the functionality to run the Dice Roller app with Vagrant+Docker. The process is automated and in order to start the app, all you need to do is as follows: 

1.) Navigate to the flask directory:

```
cd DnD-Dice-Roller/flask
```

2.) Install Vagrant on your local machine. You can download it from https://www.vagrantup.com/.

3.) Start the Vagrant virtual machine:

```
vagrant up
```

Once provisioning is completed, you can access the DnD Roller app in your web browser by navigating to:

http://192.168.111.202

This will take you to the DnD Dice Roller application, where you can input the number of rolls and view the results of dice rolls.

# Notes

- The Vagrant virtual machine is provisioned with all the necessary dependencies to run the Flask application.
- If you encounter any issues during provisioning or accessing the app, please refer to the documentation or troubleshooting guides provided by Vagrant.
- For any questions or assistance, feel free to open an issue on this repository.

Enjoy rolling your virtual dice with the DnD Dice Roller app!