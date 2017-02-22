# Rails0001
## Limit vs Take
* take return array
* limit return ActiveRecord relation which can used to chain

## How to Use CSV in ruby for write to file

```ruby

require 'csv'

HEADERS = ['x', 'y', 'z']

CSV.open('file', 'w', headers: HEADERS) do |csv|
    csv << [x, y, z]
end

# or

test = CSV.open('file', 'w', headers: HEADERS)
test.puts [x, y, x]
test.close

```

## present? vs blank? (nil?, empty?)
* nil? 単純にnilか
* empty? は[], {}, '', ""を判断 not nil
* blank?は nil? + blank?
* present?は blank?の逆、でもonly for ruby

