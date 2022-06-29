impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head == None {
            return None;
        }
        let mut list_node = head.unwrap();
        let mut node = Box::new(ListNode::new(list_node.val));
        let mut last_node;

        if list_node.next == None {
            return Some(node);
        }

        list_node = list_node.next.unwrap();
        last_node = node;

        loop{
            node = Box::new(ListNode::new(list_node.val));
            node.next = Some(last_node);

            if list_node.next != None {
                list_node = list_node.next.unwrap();
                last_node = node;
            }
            else {
                break;
            }
        }
        return Some(node);
    }
}