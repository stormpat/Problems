
fn main() {
  let d = Door { limit: 101. }; // No "0"th door.
  let open = d.open();
  let closed = d.closed();
  println!("The doors: {} are open.", &open);
  println!("The doors: {} are closed.", &closed);
}

struct Door {
  limit: f32,
}

impl Door {

  fn open(&self) -> Vec<f32> {
    let mut vect = vec![];
    for i in range(1f32, self.limit) {
      if _check(i) {
        vect.push(i);
      }
    }
    vect
  }

  fn closed(&self) -> Vec<f32> {
    let mut vect = vec![];
    for i in range(1f32, self.limit) {
      if !_check(i) {
        vect.push(i);
      }
    }
    vect
  }
}

fn _check(i: f32) -> bool {
  i.sqrt() == i.sqrt().ceil()
}
