class Dice:
    def __init__(self, dice_output_list):
        self.dice_output_list = dice_output_list
        self.current_index = 0
        
    def roll_die(self):
        if self.current_index < len(self.dice_output_list):
            roll = self.dice_output_list[self.current_index]
            self.current_index += 1
            return roll
        return None