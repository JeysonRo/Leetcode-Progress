class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = rmax = 0
        water = 0
        step = 0

        while l < r:
            step += 1
            print("step: " + str(step) + "\nl: " + str(l) + "\nr: " + str(r) + "\nwater: " + str(water) + "\n")

            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])

            if height[l] <= height[r]:
                l += 1
                water += max(0, min(lmax, rmax) - height[l])
            else:
                r -= 1
                water += max(0, min(lmax, rmax) - height[r])
            
        return water
