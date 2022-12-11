use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn get_file(path: &str) -> Vec<String> {
    let file = File::open(path).unwrap();
    let reader = BufReader::new(file);

    // Prepare Vector that contains the lines
    let mut contents: Vec<String> = vec![];

    // Read line by line
    for line in reader.lines()
    {
        let line = line.unwrap().parse::<String>().unwrap();
        contents.push(line);
    }

    return contents;
}

pub fn split_by_newline(lines: &Vec<String>) -> Vec<Vec<u32>> {
    let mut groups: Vec<Vec<u32>> = vec![vec![]];
    let mut index: usize = 0;

    for line in lines {
        if line == "" {
            groups.push(vec![]);
            index += 1;
            continue;
        }

        groups[index].push(line.parse::<u32>().unwrap());
    }

    return groups;
}

pub fn split_by_nth(lines: &Vec<String>, n: u16) -> Vec<Vec<String>> {
    let mut groups: Vec<Vec<String>> = vec![vec![]];
    let mut index: u16 = 0;

    for line in lines {
        if index == n {
            groups.push(vec![]);
            index = 0;
        }

        let last_index = groups.len()-1;

        groups[last_index].push(line.parse::<String>().unwrap());
        index += 1
    }

    return groups;
}
