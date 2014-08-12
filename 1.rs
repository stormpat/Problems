
fn main() {
  let problem = 1i;
  println!("Euler problem {} \n", problem);
  // Begin problem
  let mut sum = 0i;
  for i in range(0i, 1000i) {
    if i % 3 == 0 || i % 5 == 0 {
      sum = sum + i;
    }
  }
  println!("The sum is: {}", sum);
}