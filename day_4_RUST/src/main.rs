use std::thread;

extern crate crypto;

mod part1;
mod part2;

fn main() {
    let mut children = vec![];
    children.push(thread::spawn(|| {
           part1::solution("00000".to_string());
    }));
    children.push(thread::spawn(|| {
           part1::solution("000000".to_string());
    }));
    for child in children{
        let _ = child.join();
    }

}

