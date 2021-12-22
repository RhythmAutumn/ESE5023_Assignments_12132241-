module Solar_hour_angle

        real(4) ::h,LST
        contains
        subroutine cal2()
        write(*,*) 'Input the local solar time(in min) LST'
        read(*,*) LST

        h=15*((LST/60)-12)

        end subroutine cal2

end module Solar_hour_angle

