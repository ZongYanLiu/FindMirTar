ARGF.each do |elem|
  elem.chomp!
  fields    = elem.split("\t")
  mis_str   = fields[7]
  mis_str   = "" if mis_str.nil?
  pan_score = 0
  mimic     = [0, 0]
  p3        = [0, 0]
  p5        = [0, 0]

  mis_str.split(',').each do |mismatch|

    pos = mismatch.split(':').first.to_f + 1
    case pos
    when 2..8
      if mismatch =~ /(T>G)|(G>T)/
        mimic[0] += 1
        pan_score += 1
      else
        mimic[1] += 1
        pan_score += 2
      end
    when 1
      if mismatch =~ /(T>G)|(G>T)/
        p5[0] += 1
        pan_score += 0.5
      else
        p5[1] += 1
        pan_score += 1
      end
    else
      if mismatch =~ /(T>G)|(G>T)/
        p3[0] += 1
        pan_score += 0.5
      else
        p3[1] += 1
        pan_score += 1
      end
    end

  end

  next if pan_score > 6

  # print result

  output = fields[0, 5]
  output << pan_score << p5.join('//') << p3.join('//') << mimic.join('//')
  puts output.join("\t")

end


__END__
