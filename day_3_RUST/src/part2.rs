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
        Ok(file) => file,
    };
    let mut input = String::new();

    match file.read_to_string(&mut input){
        Ok(val) => val,
        Err(_) => panic!("Error while reading {}.",display) 
    };

    let mut loc_santa = (0,0);
	let mut loc_robo_santa = (0,0);
    let mut houses = HashMap::<(i32,i32),i32>::new();
    houses.insert((0,0),2);
    for (index,char) in input.chars().enumerate(){
		let mut loc = match index % 2{
			0	=>	&mut loc_santa,
			_	=>	&mut loc_robo_santa
		};
        *loc = match char{
            '^' => (loc.0,loc.1+1),
            '<' => (loc.0 - 1,loc.1),
            '>' => (loc.0 + 1,loc.1),
            'v' => (loc.0,loc.1 - 1),
             _   => panic!("Unknown char: {}",char)
        };
        let val = match houses.entry(*loc){
            Vacant(entry)   =>  entry.insert(0),
            Occupied(entry) =>  entry.into_mut()
        };
		// If there was no entry it will create it with value 0 and return reference to that value in val
		// if there was an entry then it returns reference to value in val
		// In both cases we will need to increment it 
        *val +=1
    }
    println!("Number of visited houses is {}",houses.len());
}

