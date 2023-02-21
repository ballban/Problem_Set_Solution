struct Solution;

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

impl Solution {
  pub fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
    let mut current = head.unwrap();
    let mut new_node: ListNode = ListNode::new(0);
    let head = &new_node.Copy();

    while current.next != None {
      current = current.next.unwrap();
      println!("{}", current.val);
      if current.val != val {
        let temp = Box::new(ListNode::new(current.val));
        new_node.next = Some(temp);
        new_node = *new_node.next.unwrap();
      }
    }
    return head.next.as_ref();
  }
}

fn main() {
  let mut head = ListNode::new(1);
  head.next = Some(Box::new(ListNode { val: (1), next: (
    Some(Box::new(ListNode { val: (1), next: (
      Some(Box::new(ListNode { val: (0), next: (
        Some(Box::new(ListNode::new(1)))
      ) })
    )) }
  ))) }));
  let result = Solution::remove_elements(Some(Box::new(head)), 1);
  println!("{}", result.unwrap().val);

  // let mut a = 1;
  // let b = Box::new(a);
  // a = 2;
  // let c = &a;
  // println!("{} {}", b, c);
}