def length_of_longest_substring(s)
    n = s.length
    set = Set.new
    max_length, i, j = 0, 0, 0
    while i < n && j < n
        if !set.include?(s[j])
            set.add(s[j])
            j += 1
            max_length = [max_length, j - i].max
        else
            set.delete(s[i])
            i += 1
        end
    end
    return max_length
end