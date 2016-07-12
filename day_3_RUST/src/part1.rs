use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use std::collections::HashMap;
use std::collections::hash_map::Entry::{Occupied,Vacant};


pub fn solution(){
	let path = Path::new("input.txt");
    let display = path.display();
    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, Error::description(&why)),
        Ok(file) => file
    };
    let mut input = String::new();

    match file.read_to_string(&mut input){
        Ok(val) => val,
        Err(_) => panic!("Error while reading {}.",display) 
    };

    let mut loc = (0,0);
    let mut houses = HashMap::<(i32,i32),i32>::new();
    houses.insert(loc,1); // insert starting point
    for char in input.chars(){
        loc = match char{
            '^' => (loc.0,loc.1+1),
            '<' => (loc.0 - 1,loc.1),
            '>' => (loc.0 + 1,loc.1),
            'v' => (loc.0,loc.1 - 1),
             _   => panic!("Unknown char: {}",char)
        };
        let val = match houses.entry(loc){
            Vacant(entry)   =>  entry.insert(0),
            Occupied(entry) =>  entry.into_mut()
        };
        *val +=1
    }
    println!("Number of visited houses is {}",houses.len());
}

