
use crypto::md5::Md5;
use crypto::digest::Digest;

pub fn solution(zeroes: String){
    let my_key = "ckczppom";
	let mut hasher = Md5::new();
    let mut x = 1;
    loop{
        hasher.reset();
        hasher.input(my_key.as_bytes());
        hasher.input(x.to_string().as_bytes());
        let hash = hasher.result_str();
        if hash.starts_with(&zeroes){
            println!("Searching for {} zeroes.",zeroes.len());
            println!("{} => {}",x,hash);
            println!("Number is {}",x);
            break;
        };
        x +=1;
    }
}

