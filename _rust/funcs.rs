

fn main() {
    let decimal = 120.4321_f32;
    let integer = decimal as u8;
    let character = integer as char;
    println!("Casting: {} -> {} -> {}", decimal, integer, character);
    let s = String::from_str("hello");
    assert_eq!(s.as_slice(), "hello");
    println!("{}", s);
    println!("{}", "helloooo".as_slice())
}