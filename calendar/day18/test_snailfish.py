import pytest

from main import add_snailfish_list
from snailfish import Snailfish

example1 = [
    "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
    "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
    "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
    "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
    "[7,[5,[[3,8],[1,4]]]]",
    "[[2,[2,2]],[8,[8,1]]]",
    "[2,9]",
    "[1,[[[9,3],9],[[9,0],[0,7]]]]",
    "[[[5,[7,4]],7],1]",
    "[[[[4,2],2],6],[8,7]]",
]

example2 = [
    "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
    "[[[5,[2,8]],4],[5,[[9,9],0]]]",
    "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
    "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
    "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
    "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
    "[[[[5,4],[7,7]],8],[[8,3],8]]",
    "[[9,3],[[9,9],[6,[4,9]]]]",
    "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
    "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
]


@pytest.mark.parametrize(
    "sf_string",
    [
        "[[[[[9,8],1],2],3],4]",
        "[7,[6,[5,[4,[3,2]]]]]",
        "[[6,[5,[4,[3,2]]]],1]",
        "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]",
    ],
)
def test_repr_from_string_matches(sf_string):
    snailfish = "[[1,2],3]"
    snailfish = sf_string
    sf = Snailfish.from_string(snailfish)
    assert snailfish == str(sf)


@pytest.mark.parametrize(
    "sf_string,reduction",
    [
        ("[[[[[9,8],1],2],3],4]", ("explode", "00000")),
        ("[7,[6,[5,[4,[3,2]]]]]", ("explode", "11110")),
    ],
)
def test_find_first_reduction(sf_string, reduction):
    snailfish = "[1,[11,[3,12]]]"
    snailfish = sf_string
    sf = Snailfish.from_string(snailfish)
    first = sf.first_reduction()
    assert first == reduction
    # assert first == ("split", "10")


def test_split():
    snailfish = "[1,[11,[3,12]]]"
    sf = Snailfish.from_string(snailfish)
    new_sf = sf.split("10")
    assert str(new_sf) == "[1,[[5,6],[3,12]]]"


def test_explode():
    snailfish = "[[[1,[2,3]],4],5]"
    sf = Snailfish.from_string(snailfish)
    new_sf = sf.explode("0010")
    assert str(new_sf) == "[[[3,0],7],5]"


@pytest.mark.parametrize(
    "sf_string,reduced",
    [
        ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
        ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
    ],
)
def test_one_operation(sf_string, reduced):
    # snailfish = "[1,[11,[3,12]]]"
    snailfish = sf_string
    sf = Snailfish.from_string(snailfish)
    first_reduction = sf.first_reduction()
    new_sf = sf.perform_op(*first_reduction)
    assert str(new_sf) == reduced


@pytest.mark.parametrize("sf_list,result", [(("[0,0]", "[1,1]"), "[[0,0],[1,1]]")])
def test_add_snailfish_list(sf_list, result):
    sum = add_snailfish_list(sf_list)
    print(sum.entries)
    assert str(sum) == result


l = [[1, 1], [2, 2], [3, 3], [4, 4]]


def simple_snail_list(num):
    return [f"[{i},{i}]" for i in range(1, num + 1)]


@pytest.mark.parametrize(
    "sf_list,result",
    [
        (simple_snail_list(4), "[[[[1,1],[2,2]],[3,3]],[4,4]]"),
        (simple_snail_list(5), "[[[[3,0],[5,3]],[4,4]],[5,5]]"),
        (simple_snail_list(6), "[[[[5,0],[7,4]],[5,5]],[6,6]]"),
        (example1, "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"),
    ],
)
def test_add_snailfish_list_and_reduce(sf_list, result):
    sum = add_snailfish_list(sf_list)
    assert str(sum) == result


@pytest.mark.parametrize(
    "snailfish,score",
    [
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
        ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
        ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
        ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
    ],
)
def test_get_magnitude(snailfish, score):
    sf = Snailfish.from_string(snailfish)
    assert sf.get_magnitude() == score


def test_get_magnitude_of_sum():
    sum = add_snailfish_list(example2)
    assert str(sum) == "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"
    magnitude = sum.get_magnitude()
    assert magnitude == 4140
