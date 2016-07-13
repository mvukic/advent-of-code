use std::error::Error;
use std::iter::Iterator;
use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::path::Path;
use std::collections::HashMap;


pub fn solution(){
    let path = Path::new("input.txt");
    let display = path.display();
    let file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, Error::description(&why)),
        Ok(file) => file
    };
    let reader = BufReader::new(file);
    let lines = reader.lines();
    let mut matrix: HashMap<(u32,u32),u32> = HashMap::with_capacity(1000*1000);
    println!("INIT start part1");
    for x in 0..1000{
        for y in 0..1000{
            matrix.insert((x,y),0);
        };
    };
    println!("INIT end part1");
    for line in lines{
        let l = line.unwrap();
        let mut split = l.split(" ");
        let vec: Vec<&str> = split.collect();
        let vec_start:Vec<&str>;
        let vec_end:Vec<&str>;
        if vec.len() == 5{
            split = vec[2].split(",");
            vec_start= split.collect();
            split = vec[4].split(",");
            vec_end = split.collect();
        }else{
            split = vec[1].split(",");
            vec_start= split.collect();
            split = vec[3].split(",");
            vec_end = split.collect();
        };
        let (s1,s2) = (vec_start[0].parse::<u32>().unwrap(),vec_start[1].parse::<u32>().unwrap());
        let (e1,e2) = (vec_end[0].parse::<u32>().unwrap(),vec_end[1].parse::<u32>().unwrap());
        if vec[0].eq("toggle"){
            for x in s1..e1+1{
                for y in s2..e2+1{
                    let val = matrix.get_mut(&(x,y)).unwrap();
                    *val += 2;
                };
            };
        }else if vec[1].eq("off"){
            for x in s1..e1+1{
                for y in s2..e2+1{
                    let val = matrix.get_mut(&(x,y)).unwrap();
                    if *val > 0{
                        *val -= 1;   
                    };
                };
            };
        }else{
            for x in s1..e1+1{
                for y in s2..e2+1{
                    let val = matrix.get_mut(&(x,y)).unwrap();
                    *val += 1;
                };
            };            
        };
    };
    let mut c = 0;
    for val in matrix.values(){
        c += *val;
    };
    println!("Total brightness is {}",c);
}

