use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    let path = Path::new("input.txt");
    let display = path.display();
    let mut floor: i32 = 0;
    let mut searching_basement:bool = true;
    let mut index_to_basement=0;
    let mut s = String::new(); 

    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why.description()),
        Ok(file) => file,
    };

    match file.read_to_string(&mut s) {
        Err(why) => panic!("couldn't read {}: {}", display,why.description()),
        Ok(_)    => println!("File {} read succefully!",display)
    }
    
    for (index,c) in s.chars().enumerate(){
        match c{
            '(' => floor += 1,
            ')' => floor -= 1,
            ch  => println!("Unknown character: {}",ch)
        }
        if searching_basement && floor == -1{
            index_to_basement = index+1;
            searching_basement = false;
        }
    }
    println!("First ndex for basement is {}",index_to_basement);
    println!("Floor is {}",floor);
}

