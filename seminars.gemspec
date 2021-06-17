# coding: utf-8

Gem::Specification.new do |spec|
  spec.name          = "seminars"
  spec.version       = "0.1.0"
  spec.authors       = ["Dario Prandi"]
  spec.email         = ["dario.prn@gmail.com"]

  spec.summary       = "ICode seminars page"
  spec.homepage      = "http://www.ccccc.com"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r{^(assets|_layouts|_includes|_sass|LICENSE|README)}i) }

  spec.add_runtime_dependency "jekyll", ">= 3.3", "< 5.0"

  spec.add_development_dependency "bundler"
  spec.add_development_dependency "rake", "~> 12.3"
end
