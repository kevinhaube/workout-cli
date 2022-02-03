from uuid import UUID
import inquirer

from .Enums import *

class Movement:

    def __init__(self,
                workout_id,
                name,
                group,
                sets,
                reps,
                total_weight) -> None:
        self.workout_id = workout_id
        self.group = group
        self.name = name
        self.sets = int(sets),
        self.reps = int(reps),
        self.total_weight = float(total_weight)
        self.volume = int(reps) * int(sets) * float(total_weight)

    # CLI process to make a Movement
    def make(workout_id: UUID):
        gr_question = [
            inquirer.List(
                'group', 
                message="Muscle group",
                choices=Volume_Enums.get_all()
            )
        ]
        gr_answer = inquirer.prompt(gr_question)
        questions = [
            inquirer.List(
                'name', 
                message="Movement name",
                choices=get_group(gr_answer['group'])),
            inquirer.Text('sets', message="Sets"),
            inquirer.Text('reps', message="Reps"),
            inquirer.Text('weight', message="Weight"),
            
        ]
        answers = inquirer.prompt(questions)
        return Movement(
                workout_id,
                answers['name'],
                gr_answer['group'],
                answers['sets'],
                answers['reps'],
                answers['weight']
        )

    # Iterates to build a list of Movements
    def builder(i: int, workout_id: UUID):
        j = 0
        movements = []
        while j < i:
            print('\n')
            movement = Movement.make(workout_id)
            movements.append(movement)
            j += 1
        return movements

    def to_dict(self):
        return {
            'name': [self.name],
            'group': [self.group],
            'sets': [self.sets],
            'reps': [self.reps],
            'weight': [self.total_weight],
            'volume': [self.volume]
        }

def to_dict_from_list(movements: list[Movement]):
    name = []
    group = []
    sets = []
    reps = []
    weight = []
    volume = []
    
    for mv in movements:
        name.append(mv.name)
        group.append(mv.group)
        sets.append(mv.sets)
        reps.append(mv.reps)
        weight.append(mv.total_weight)
        volume.append(mv.volume)

    return {
        'name': name,
        'group': group,
        'sets': sets,
        'reps': reps,
        'weight': weight,
        'volume': volume
    }



# Returns the enumerated movement names for the selected muscle group
def get_group(group_answer: str):
    if group_answer == Volume_Enums.QUADS:
        return Quad_Movements.get_all()
    if group_answer == Volume_Enums.HAMSTRINGS:
        return Ham_Movements.get_all()
    if group_answer == Volume_Enums.CALF:
        return Calf_Movements.get_all()
