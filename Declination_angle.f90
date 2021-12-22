module Declination_angle

implicit none

        integer :: d
        real(8) :: a,b,pi

contains
        subroutine cal()
        pi=3.14159265
        write(*,*) 'Input the number of days since Jan. 1st d'
        read(*,*) d

        b=COS(pi/180*(360/365.24)*(d+10)+(360/pi)*0.0167*SIN((pi/180*360/365.24)*(d-2)))

        a=(ASIN(SIN(-23.44*pi/180)*b))*180/pi

        end subroutine cal

end module Declination_angle
