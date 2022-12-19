from pathlib import Path

from delta_utils import get_discrete_choose_move_out_checker
from delta_utils.check_submission import check_submission as _check_submission

from game_mechanics import PongEnv, load_network


def check_submission(team_name: str) -> None:
    example_state, _, _, _ = PongEnv(lambda x: x).reset()
    user_pkl_file = load_network(team_name)

    possible_outputs = [-1, 0, 1]

    _check_submission(
        example_choose_move_input={"state": example_state, "neural_network": user_pkl_file},
        check_choose_move_output=get_discrete_choose_move_out_checker(
            possible_outputs=possible_outputs,
        ),
        current_folder=Path(__file__).parent.resolve(),
    )
