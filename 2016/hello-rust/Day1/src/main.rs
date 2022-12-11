use std::fs;

fn main() {
    let contents = fs::read_to_string("./data.txt").expect("Cant read");
    let directions = contents.split(", ");
    let current_direction = 0;
    let total_x = 0;
    for direction in directions {
        println!("Direction: {}", direction);
        
    }
}
