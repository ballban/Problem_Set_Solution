struct Solution;

impl Solution {
  pub fn can_reach(arr: Vec<i32>, start: i32) -> bool {
    let len = arr.len();
    let u_start = start as usize;
    let mut visited = vec![false; arr.len()];
    let mut stack = vec![start as usize; 1];
    while stack.len() > 0 {
      let i = stack.pop().unwrap();
      visited[i] = true;

      let left = i as i32 - arr[i];
      if left >= 0 {
        if arr[left as usize] == 0 {
          return true;
        }
        if visited[left as usize] == false {
          stack.push(left as usize);
        }
      }

      let right = i + arr[i] as usize;
      if right < len {
        if arr[right] == 0 {
          return true;
        }
        if visited[right] == false {
          stack.push(right);
        }
      }
    }

    return false;
  }

  pub fn can_reach2(arr: Vec<i32>, start: i32) -> bool {
    let mut visited = vec![false; arr.len()];
    return Solution::_can_reach(&arr, &mut visited, start);
  }

  pub fn _can_reach(arr: &Vec<i32>, visited: &mut Vec<bool>, i: i32) -> bool {
    //println!("{:?}", count);
    if arr[i as usize] == 0 {
      return true;
    }

    if visited[i as usize] {
      return false;
    }

    visited[i as usize] = true;
    let right = i + arr[i as usize];
    let left = i - arr[i as usize];
    let mut result = false;
    if right < arr.len() as i32 {
      result = Solution::_can_reach(arr, visited, right);
    }

    if result {
      return result;
    }

    if left >= 0 {
      return Solution::_can_reach(arr, visited, left);
    }

    return false;
  }
}

fn main() {
  let arr = vec![3,0,2,1,2];
  let start = 2;
  println!("{}", Solution::can_reach(arr, start));
}