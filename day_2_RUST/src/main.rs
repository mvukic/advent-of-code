use std::error::Error;
use std::iter::Iterator;
use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    let path = Path::new("input.txt");
    let display = path.display();
    let file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, Error::description(&why)),
        Ok(file) => file,
    };
    let reader = BufReader::new(file);
    let lines = reader.lines(); 

    let mut final_size=0;
    let mut ribbon_size = 0;
    for line in lines {
        let l = line.unwrap(); 
        let split = l.split("x");
        let vec = split.collect::<Vec<&str>>();
        let (l,w,h) = (vec[0].parse::<u32>().unwrap(),vec[1].parse::<u32>().unwrap(),vec[2].parse::<u32>().unwrap());
        let dim = [2*l*w,2*w*h,2*h*l];
        let mut dim_sizes = [l,w,h];
        let size = dim[0]+dim[1]+dim[2] + dim.iter().min().unwrap()/2;
        dim_sizes.sort();
        ribbon_size += dim_sizes[0]*2+dim_sizes[1]*2+l*w*h;
        final_size += size;
    }
    println!("Final ribbon size is {}",ribbon_size);
    println!("Final size is {}",final_size);
}

