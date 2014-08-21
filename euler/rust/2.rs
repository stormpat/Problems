

fn main() {
  let problem = 2i;
  println!("Euler problem {} \n", problem);
  // Begin problem
  println!("{}", evens());
}

fn evens() {
  let limit = 4000000i;
  let mut even = 0i;
  for i in range(0i, 40i) {
    let _cache = fib(i);
    if _cache % 2 == 0 { even = even + _cache; }
    if _cache >= limit { break; }
  }
  println!("Fibonacci evens before {}: {}", limit, even);
}

fn fib(num: int) -> int {
  if num < 2 {
    return 1;
  } else {
    return fib(num - 2) + fib(num - 1);
  }
}
