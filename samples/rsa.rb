def is_prime(num)
  if num == 2 or num == 3
    return true
  end

  if num < 2 or num % 2 == 0
    return false
  end

  (3 .. Integer(num**0.5)+2).step(2).to_a.each do |n|
    if num % n == 0
      return false
    end
    return true
  end
end

def gcd (a, b)

  while a != 0
    c = a; a = b%a; b = c
  end

  return b

end

def mul_inverse(e, phi)
  d = 0
  x1 = 0
  x2 = 1
  y1 = 1
  temp_phi = phi

  while e > 0
    temp1 = temp_phi/e
    temp2 = temp_phi - temp1 * e
    temp_phi = e
    e = temp2

    x = x2- temp1* x1
    y = d - temp1 * y1

    x2 = x1
    x1 = x
    d = y1
    y1 = y
  end

  if temp_phi == 1
    return d + phi
  end
end


def gen_keypair(p, q)
  if not (is_prime(p) and is_prime(q))
    puts 'Not prime'
    exit!(1)
  end

  if p == q
    printf("%s\n", "p and q shouldn't same")
    exit!(1)
  end

  puts

  phi = (p - 1) * (q - 1)
  n = p * q
  e = Random.rand(2 .. phi)

  g = gcd(e, phi)
  while g != 1
    e = Random.rand(2 .. phi)
    g = gcd(e, phi)
  end

  d = mul_inverse(e, phi)

  return [[e, n], [d, n]]
end

def encrypt(pri, mes)
  key, n = pri
  mes.split("").map do |c|
    c.ord ** key % n
  end
end

def decrypt(pub, en_mes)
  key, n = pub
  en_mes.map do |c|
    (c ** key % n).chr
  end
end

def main
  puts 'Input P value:'
  p = Integer(gets())

  puts 'Input Q value:'
  q = Integer(gets())

  pub, pri = gen_keypair(p, q)
  puts 'Input Encrypt messages:'
  message = gets()
  encrypted_msg = encrypt(pri, message)
  puts 'encrypt messages'
  puts encrypted_msg.join(" , ")
  puts 'decrypt messages'
  puts decrypt(pub, encrypted_msg).join("")
end

main()