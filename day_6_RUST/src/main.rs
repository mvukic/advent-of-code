use std::thread;

mod part1;
mod part2;

fn main() {
    let mut children = vec![];
    children.push(thread::spawn(move || {
           part1::solution();
    }));
    children.push(thread::spawn(move || {
           part2::solution();
    }));
    for child in children{
        let _ = child.join();
    }
}