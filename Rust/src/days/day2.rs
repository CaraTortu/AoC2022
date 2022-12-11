use std::collections::HashMap;
use super::lib::read_file;

pub fn main() {
    let input = read_file::get_file("./src/inputs/solutions/day2");

    println!("Day 2 solution A: {}", part_a(&input));
    println!("Day 2 solution B: {}\n", part_b(&input));
}

fn part_a(input: &Vec<String>) -> u32 {
    let game_options = HashMap::from([
        ("A", HashMap::from([
            ("X", 4),
            ("Y", 8),
            ("Z", 3)
        ])),
        ("B", HashMap::from([
            ("X", 1),
            ("Y", 5),
            ("Z", 9)
        ])),
        ("C", HashMap::from([
            ("X", 7),
            ("Y", 2),
            ("Z", 6)
        ]))
    ]);

    let mut total_score: u32 = 0;

    for line in input {
        let splitted: Vec<&str> = line.split(" ").collect();
        total_score += game_options[splitted[0]][splitted[1]];
    }

    return total_score
}
 
fn part_b(input: &Vec<String>) -> u32 {
    let game_options = HashMap::from([
        ("A", HashMap::from([
            ("X", 3),
            ("Y", 4),
            ("Z", 8)
        ])),
        ("B", HashMap::from([
            ("X", 1),
            ("Y", 5),
            ("Z", 9)
        ])),
        ("C", HashMap::from([
            ("X", 2),
            ("Y", 6),
            ("Z", 7)
        ]))
    ]);

    let mut total_score: u32 = 0;

    for line in input {
        let splitted: Vec<&str> = line.split(" ").collect();
        total_score += game_options[splitted[0]][splitted[1]];
    }

    return total_score
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_part_a() {
        let input: Vec<String> = read_file::get_file("./src/inputs/tests/day2");
        assert_eq!(part_a(&input), 15);
    }

    #[test]
    fn test_part_b() {
        let input: Vec<String> = read_file::get_file("./src/inputs/tests/day2");
        assert_eq!(part_b(&input), 12);
    }
}