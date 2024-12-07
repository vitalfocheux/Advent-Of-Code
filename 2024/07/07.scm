#lang racket

(define (correct-test-combined r values i value test-type)
  (if (= i (length values))
      (= r value)
      (let* ((add (+ value (list-ref values i)))
             (mul (if (= value 0)
                      (list-ref values i)
                      (* value (list-ref values i))))
             (concat (if (eq? test-type 'concat)
                         (string->number (string-append (number->string value) (number->string (list-ref values i))))
                         value)))
        (or (correct-test-combined r values (+ i 1) add test-type)
            (correct-test-combined r values (+ i 1) mul test-type)
            (if (eq? test-type 'concat)
                (correct-test-combined r values (+ i 1) concat test-type)
                #f)))))

(define (part1 input)
  (define (parse-line line)
    (let* ((split (string-split line ":"))
           (r (string->number (car split)))
           (values (map string->number (string-split (cadr split) " ")) ))
      (if (correct-test-combined r values 0 0 'default)
          r
          0)))
  (apply + (map parse-line (string-split input "\n"))))

(define (part2 input)
(define (parse-line line)
(let* ((split (string-split line ":"))
        (r (string->number (car split)))
        (values (map string->number (string-split (cadr split) " ")) ))
    (if (correct-test-combined r values 0 0 'concat)
        r
        0)))
(apply + (map parse-line (string-split input "\n"))))

(define (read-file filename)
  (with-input-from-file filename
    (lambda ()
      (let ((content (port->string (current-input-port))))
        content))))

(define (absolute-path filename)
  (build-path (current-directory) filename))

(define input (read-file (absolute-path "07.txt")))
(displayln (part1 input)) 
(displayln (part2 input)) 