

//return max(a * b for a in range(1,1000) for b in range(a,1000) if str(a * b) == str(a * b)[::-1])
fn main() {
  let problem = 4i;
  println!("Euler problem {} \n", problem);
  // Begin problem
}

fn palindrome() -> int {
  for n in range(100,1000) {
    for nx in range(100,1000) {
      let mut sum = n * nx;
      let mut largest = 0;
      if to_str(sum).rev_iter() == to_str(sum) && sum > largest {
        largest = sum
      }
    }
  }
}
