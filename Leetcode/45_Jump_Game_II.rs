struct Solution;

impl Solution {
  // pub fn max_area(height: Vec<i32>) -> i32 {
  //   let mut result = 0;
  //   for (i, n) in height.iter().enumerate() {
  //     println!("{i} {n}");
  //     let target_index = Solution::find_num(&height, i, *n)  as i32;
  //     println!("targetIndex: {target_index}");
  //     let max_value =((i  as i32) - target_index).abs() * n;
  //     println!("max_value: {max_value}");
  //     result = std::cmp::max(max_value, result);
  //   }
  //   return result;
  // }

  // pub fn find_num(height: &Vec<i32>, index: usize, num: i32) -> usize {
  //   let mut left:usize = 0;
  //   let mut right:usize = height.len() - 1;
  //   loop {
  //     if left == index {
  //       break;
  //     }
  //     if height[left] >= num {
  //       break;
  //     }

  //     left += 1;
  //   }

  //   loop {
  //     if right == index {
  //       break;
  //     }
  //     if height[right] >= num {
  //       break;
  //     }

  //     right -= 1;
  //   }

  //   let left_d = index - left;
  //   let right_d = right - index;

  //   if left_d > right_d {
  //     return left;
  //   } else {
  //     return right;
  //   }
  // }

  pub fn max_area(height: Vec<i32>) -> i32 {
    let mut result = 0;
    let mut val;
    let mut left = 0;
    let mut right = height.len() - 1;

    while left < right {
      let right_val = height[right];
      let left_val = height[left];
      if left_val > right_val {
        val = (right - left) as i32 * right_val;
        right -= 1;
      } else if left_val < right_val {
        val = (right - left) as i32 * left_val;
        left += 1;
      } else {
        val = (right - left) as i32 * right_val;
        right -= 1;
        left += 1;
      }
      result = std::cmp::max(result, val);
    }
    return result;
  }
}

fn main() {
  let height = vec![1,8,6,2,5,4,8,3,7];
  //height = vec![1,1];

  println!("{}", Solution::max_area(height));
}