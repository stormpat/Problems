
fn main() {
  let problem = 3i;
  println!("Euler problem {} \n", problem);
  // Begin problem
  let factors = prime_fac(600851475143);
  println!("{}", factors.last().unwrap());
}

fn prime_fac(num: int) -> Vec<int> {
  let mut vect = vec![];
  let mut i : int = 2;
  let mut n = num;

  while (i * i) <= n {
    if n % i == 0 {
      vect.push(i);
      n = n / i;
    } else {
      i = i + 1;
    }
  }
  if n != 1 {
    vect.push(n);
  }
  return vect;
}
