def open_box(count):
    def helper(count):
        print("Open")
        count -= 1
        if count == 0:
            print("Get Ring")
            return
        helper(count)
    
    helper(count)

open_box(count=10)