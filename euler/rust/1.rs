
use std::iter::AdditiveIterator;

fn main() {
  let problem = "1: Multiples of 3 and 5";
  println!("Euler problem {} \n", problem);
  // Begin problem
  println!("Procedural: {}", procedural());
  println!("Functional: {}", functional());
}

fn functional() -> int {
  let it = range(0i, 1000);
  it.filter(|n| n % 3 == 0 || n % 5 == 0).sum()
}

fn procedural() -> int {
  let mut sum = 0i;
  for i in range(0i, 1000) {
    if i % 3 == 0 || i % 5 == 0 {
      sum = sum + i;
    }
  }
  sum
}

#[test]
fn test_problem() {
  let p = procedural();
  let f = functional();
  assert!(p == 233168);
  assert!(f == 233168);
}

