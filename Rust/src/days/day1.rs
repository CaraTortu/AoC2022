use super::lib::read_file;

pub fn main() {
    let input = read_file::get_file("./src/inputs/solutions/day1");
    let groups: Vec<Vec<u32>> = read_file::split_by_newline(&input);

    println!("Day 1 solution A: {}", part_a(&groups));
    println!("Day 1 solution B: {}\n", part_b(&groups));
}

fn part_a(input: &Vec<Vec<u32>>) -> u32 {
    let sums: Vec<u32> = input.iter().map(|d| d.iter().sum::<u32>()).collect();
    return *sums.iter().max().unwrap()
}
 
fn part_b(input: &Vec<Vec<u32>>) -> u32 {
    let mut sums: Vec<u32> = input.iter().map(|d| d.iter().sum::<u32>()).collect();
    
    sums.sort();
    sums.reverse();

    return sums[0..3].iter().sum::<u32>()
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_part_a() {
        let input: Vec<String> = read_file::get_file("./src/inputs/tests/day1");
        let groups: Vec<Vec<u32>> = read_file::split_by_newline(&input);

        assert_eq!(part_a(&groups), 24000);
    }

    #[test]
    fn test_part_b() {
        let input: Vec<String> = read_file::get_file("./src/inputs/tests/day1");
        let groups: Vec<Vec<u32>> = read_file::split_by_newline(&input);
        
        assert_eq!(part_b(&groups), 45000);
    }
}