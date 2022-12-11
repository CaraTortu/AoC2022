use super::lib::read_file;

pub fn main() {
    let input = read_file::get_file("./src/inputs/solutions/day3");

    println!("Day 3 solution A: {}", part_a(&input));
    println!("Day 3 solution B: {}\n", part_b(&input));
}

fn get_char_value(c: char) -> u32 {
    ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        .chars()
        .position(|d| d == c)
        .unwrap()
        + 1) as u32
}

fn part_a(input: &Vec<String>) -> u32 {
    let mut total_score: u32 = 0;

    for line in input {
        let line: Vec<&str> = line.split("").filter(|c| *c != "").collect();
        let part_size = line.len() / 2;

        let elf_a = &line[0..part_size];
        let elf_b = &line[part_size..];

        for c in elf_a {
            if elf_b.contains(c) {
                total_score += get_char_value(c.chars().nth(0).unwrap());
                break;
            }
        }
    }

    return total_score;
}

fn part_b(input: &Vec<String>) -> u32 {
    let mut groups: Vec<Vec<String>> = read_file::split_by_nth(input, 3);
    groups = groups.into_iter().filter(|d| d.len() != 0).collect();

    let mut total_score: u32 = 0;

    for group in groups {
        for c in group[0].chars() {
            if group[1].contains(c) && group[2].contains(c) {
                total_score += get_char_value(c);
                break;
            }
        }
    }

    return total_score;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_a() {
        let input: Vec<String> = read_file::get_file("./src/inputs/tests/day3");
        assert_eq!(part_a(&input), 157);
    }

    #[test]
    fn test_part_b() {
        let input: Vec<String> = read_file::get_file("./src/inputs/tests/day3");
        assert_eq!(part_b(&input), 70);
    }
}
