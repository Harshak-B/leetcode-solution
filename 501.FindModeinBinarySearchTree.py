class Solution:
  def findMode(self, root: Optional[TreeNode]) -> List[int]:
    # Initialize instance variables to keep track of the mode, previous node,
    # count, and maximum count.
    self.ans = []  # List to store the mode values
    self.pred = None  # The previous node
    self.count = 0  # Count of the current value
    self.maxCount = 0  # Maximum count seen so far

    # Helper function to update the count and mode values
    def updateCount(root: Optional[TreeNode]) -> None:
      if self.pred and self.pred.val == root.val:
        # If the current node's value is the same as the previous one,
        # increment the count.
        self.count += 1
      else:
        # If the values are different, reset the count to 1.
        self.count = 1

      if self.count > self.maxCount:
        # If the current count is greater than the maximum count seen so far,
        # update the maximum count and reset the mode list with the current value.
        self.maxCount = self.count
        self.ans = [root.val]
      elif self.count == self.maxCount:
        # If the current count is equal to the maximum count, add the value to the mode list.
        self.ans.append(root.val)

      self.pred = root  # Update the previous node.

    # Helper function to perform an in-order traversal of the tree.
    def inorder(root: Optional[TreeNode]) -> None:
      if not root:
        return

      inorder(root.left)  # Recursively visit the left subtree.
      updateCount(root)  # Update count and mode values based on the current node.
      inorder(root.right)  # Recursively visit the right subtree.

    # Start the in-order traversal from the root.
    inorder(root)
    return self.ans  # Return the list of mode values.

