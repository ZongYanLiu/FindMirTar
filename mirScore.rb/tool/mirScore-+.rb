puts "Tag_ID\tStrand\tContig_Name\tTarget_site\tTag_sequence\tPanalty_Score\t5'region\t3'region\tCenter_region"

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
    when 9, 10, 11
      if mismatch =~ /(G>A)|(T>C)/
        mimic[0] += 1
        pan_score += 0.5
      else
        mimic[1] += 1
        pan_score += 1
      end
    when 1..8
      if mismatch =~ /(G>A)|(T>C)/
        p5[0] += 1
        pan_score += 0.5
      else
        p5[1] += 1
        pan_score += 1
      end
    else
      if mismatch =~ /(G>A)|(T>C)/
        p3[0] += 1
        pan_score += 0.5
      else
        p3[1] += 1
        pan_score += 1
      end
    end

  end

  next if pan_score > 4

  # print result

  output = fields[0, 5]
  output << pan_score << p5.join('//') << p3.join('//') << mimic.join('//')
  puts output.join("\t")

end


__END__
