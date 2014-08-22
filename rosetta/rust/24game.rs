
extern crate debug;
extern crate rand;

use std::fmt::Formatter;
use std::fmt::Show;
use std::fmt;
use std::rand::distributions::{IndependentSample, Range};
use std::os;
use std::default::Default;

fn main() {
  let args = os::args();
  let nimi = args.get(2);
  println!("{:?}", nimi);
  let g = Game { name: String::from_str("MO"), ..Default::default() };
  println!("{}", g.random())
  println!("{}", g)
  println!("{}", g.getter())
}

struct Game {
  name: String,
  tokens: &'static str,
}

impl Default for Game {
  fn default() -> Game {
    Game { name: String::from_str(""), tokens: "+ + * - /" }

  }
}
impl fmt::Show for Game {
  fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
      write!(f, "Hi: {}", self.tokens)
  }
}

impl Game {
  // let collected_iterator: Vec<int> = range(0i, 10).collect();

  fn random(&self) -> uint {
    let between = Range::new(1u, 10);
    let mut rng = std::rand::task_rng();
    let mut sum = 0;
    for _ in range(1u, 2) {
        sum += between.ind_sample(&mut rng);
    }
    sum
  }

  fn getter(&self) {
    println!("NAME: {}, TOKENS: {}", self.name, self.tokens);
  }


}



/*
  fn seed(&self) -> Vec<int> {
    let mut vect = vec![];
    for i in range(1i,5) {
       // There must be a better way.
       // Maybe something like random from range?
      let mut n: f64 = rand::random();
      n = n * 10.;
      if n < 1. { n = n + 1.; }
      vect.push(n as int)
    }
    vect
  }
 */